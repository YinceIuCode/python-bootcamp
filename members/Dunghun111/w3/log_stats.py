from statistics import quantiles


def analyse(pairs : list[tuple]) -> dict:
    """Analyze route data give list of pairs for (route_name, latency(ms))"""
    route_data_dict = {}
    analysed_data = {}
    
    for pair in pairs:
        if route_data_dict.get(pair[0]) == None:
            route_data_dict[pair[0]] = []
            
        route_data_dict[pair[0]].append(pair[1])
    
    for key in route_data_dict.items():
        analysed_data[key] = {
            "counts" : int,
            "p95" : float,
            "slowest" : float,
        }
        
        analysed_data[key]["counts"] = len(route_data_dict[key])
        analysed_data[key]["p95"] = quantiles(route_data_dict[key], n=100, method="inclusive")[94]
        analysed_data[key]["slowest"] = max(route_data_dict[key])
    
    return analysed_data

test = [("a", 1), ("a", 2), ("a", 3), ("b", 1), ("b", 2)]
print(analyse(test))