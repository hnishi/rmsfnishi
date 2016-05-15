#include"nlib.h"
#include"inpnishi.h"

using namespace std;

int quatnishi(Inp_nishi);

int main(int argc, char *argv[]){
   cout<<"Version info. rmsfnishi v2.0 ; <- quatnishi v1.4.1 \n";
   cout<<"extrnishi \n";

// ##################### ARGUMENT HANDLING ##########################
// argv[1]: input parameter file
  if( argv[1]==NULL ){
    puts("No ARGUMEMTS");
    puts("USAGE: ./a.out (argv[1]: input parameter file)" );
    return 1;
  }
  cout<<"Your input-parameter file: "<<argv[1]<<endl;

// INPUT_PARAMETERS
   //Inp_nishi inp1( "parameter.txt" );
   Inp_nishi inp1( argv[1] );
   
// DO quatnishi
   quatnishi(inp1);
  
// END
	cout<<"\nit took "<<(float)clock()/CLOCKS_PER_SEC<<" sec of CPU to execute this program"<<endl;
	return 0;
}
