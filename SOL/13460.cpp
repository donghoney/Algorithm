#include <iostream>

using namespace std;

class Rotation {
    private:
    public:
        void Up(){

        }

        void Right(){

        }

        void Left(){

        }

        void Down(){
            
        }
};

int main(){
    int row, col;

    cin >> row >> col;

    char box[row][col];
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            cin >> box[i][j];
        }
    } 
}