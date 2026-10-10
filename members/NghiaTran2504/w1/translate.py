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
def transpose(matrix_2d: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix_2d)]
        

