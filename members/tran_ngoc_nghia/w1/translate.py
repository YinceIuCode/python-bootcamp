"""C++ code snippet:

vector<vector<int>> TransposeMatrix (vector<vector<int>>& matrix_2d){
    int row = matrix_2d.size();
    int col = matrix_2d[0].size();
    vector<vector<int>> transpose_matrix;
    for (int j = 0; j < col; ++j) {
        vector <int> v;
        for (int i = 0; i < row; ++i) {
            v.push_back(matrix_2d[i][j]);
        }
        transpose_matrix.push_back(v);
    }

    return transpose_matrix;
} """

# Python code:
def TransposeMatrix(matrix_2d: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix_2d)]
        
def create_matrix(rows: int, cols: int) -> list[list[int]]:
    matrix = []
    count = 0

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(count)
            count += 1
        matrix.append(row)

    return matrix

rows = int(input("Enter row(s): "))
cols = int(input("Enter col(s): "))
matrix_2d = create_matrix(rows, cols)
transpose_matrix = TransposeMatrix(matrix_2d)

for row in transpose_matrix:
    for col in row:
        print(col, end = " ")
    print()


