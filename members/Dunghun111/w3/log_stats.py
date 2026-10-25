from statistics import quantiles


def analyse(pairs : list[tuple]) -> dict:
    """Analyze route data give list of pairs for (route_name, latency(ms))"""
    route_data_dict = {}
    analysed_data = {}
    
    for pair in pairs:
        if route_data_dict.get(pair[0]) == None:
            route_data_dict[pair[0]] = []
            
        route_data_dict[pair[0]].append(pair[1])
    
    analysed_data = {
        "counts" : {},
        "p95" : {},
        "slowest" : None,
    }
    
    for key_tuple in route_data_dict.items():
        key = key_tuple[0]
        analysed_data["counts"][key] = len(route_data_dict[key])
        analysed_data["p95"][key] = quantiles(route_data_dict[key], n=100, method="exclusive")[94]
        analysed_data["p95"][key] = min(max(route_data_dict[key]), analysed_data["p95"][key])
        
        if analysed_data["slowest"] == None or max(route_data_dict[analysed_data["slowest"]]) < max(route_data_dict[key]):
            analysed_data["slowest"] = key
                    
    return analysed_data

print(analyse([("fee", 100), ("fee", 300), ("rag", 900), ("rag", 1100), ("fee", 200)]))