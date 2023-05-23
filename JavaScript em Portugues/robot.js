//https://www.youtube.com/watch?v=T78Q7K3c11s

include <Trade/Trade.mqh>

CTrade trade;

int OnInit(){

   return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason){
   
}

void OnTick(){

   static datetime timestamp;
   datetime time = iTime(_Symbol,PERIOD_CURRENT,0);
   if(timestamp != time){
      timestamp = time;

      static int handleSlowMa = iMA(_Symbol,PERIOD_CURRENT,2,0,MODE_SMMA,PRICE_CLOSE); //Get the moving average
      double slowMaArray[]; //Array variable 
      CopyBuffer(handleSlowMa,0,1,2,slowMaArray);// get he info we want from the moving average and store in the Array variable
      ArraySetAsSeries(slowMaArray,true);
      
      static int handleFastMa = iMA(_Symbol,PERIOD_CURRENT,9,0,MODE_EMA,PRICE_CLOSE);
      double fastMaArray[]; //Array variable 
      CopyBuffer(handleFastMa,0,1,2,fastMaArray);// get he info we want from the moving average and store in the Array variable
      ArraySetAsSeries(fastMaArray,true);
      
      if(fastMaArray[0] < slowMaArray [0] && fastMaArray[1] > slowMaArray[1]){
         Print("Eliud Compra");
         double ask = SymbolInfoDouble(_Symbol,SYMBOL_ASK);
         double sl = ask - 10000 * SymbolInfoDouble(_Symbol,SYMBOL_POINT);
         double tp = ask + 15000 * SymbolInfoDouble(_Symbol,SYMBOL_POINT);
         trade.Buy(0.50,_Symbol,ask,sl,tp,"Tis is a buy");
      }
      if(fastMaArray[0] > slowMaArray [0] && fastMaArray[1] < slowMaArray[1]){
         Print("Eliud Venda");
         double bid = SymbolInfoDouble(_Symbol,SYMBOL_BID);
         double sl = bid + 10000 * SymbolInfoDouble(_Symbol,SYMBOL_POINT);
         double tp = bid - 15000 * SymbolInfoDouble(_Symbol,SYMBOL_POINT);
         trade.Sell(0.50,_Symbol,bid,sl,tp,"Tis is a sell");
      
      }
     
      Comment ("\nslowMaArray[0]: ",slowMaArray[0],
               "\nslowMaArray[0]: ",slowMaArray[1],
               "\nfastMaArray[0]: ",fastMaArray[0],
               "\nfastMaArray[0]: ",fastMaArray[1]);
               
   }
}

