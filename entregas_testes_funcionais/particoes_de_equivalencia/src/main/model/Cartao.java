package model;

public class Cartao {
	public String numero;
	public String bandeira;

    private static final String[] bandeiras = {"Visa", "Mastercard", "American Express", "En Route", "Diner's CLub"};
    
    public static boolean isNumber(String n) {
        try {
            double d = Double.valueOf(n).doubleValue();
            return true;
        } catch (NumberFormatException e) {
            e.printStackTrace();
            return false;
        }
    }
	
	public static boolean numDigitos(String numCartao){
		int digito = numCartao.length();
		if(digito < 13 || digito > 16){
			return false;
		}
		else{
			return true;
		}
	}
    
    public static String validaBandeira(String numCartao) {
        String bandeira = "";
		int digitos = 0;
		if(numDigitos(numCartao)){
			digitos = numCartao.length();
		}
		
		String digito1 = numCartao.substring(0, 1);
        String digito2 = numCartao.substring(0, 2);
        String digito3 = numCartao.substring(0, 3);
        String digito4 = numCartao.substring(0, 4);
		
		switch (digitos) {
		  case 13:
			if (digito1.equals("4")) bandeira = "VISA";
			else bandeira = "INVALIDO";			
			break;
		  case 14:
			if (digito2.equals("36") || digito2.equals("38") || (digito3.compareTo("300") >= 0 && digito3.compareTo("305") <= 0)) bandeira = "DINERS CLUB";
			else bandeira = "INVALIDO";
			break;
		  case 15:
			if (digito2.equals("34") || digito2.equals("37")) bandeira = "AMERICAN EXPRESS"; 
			else if (digito4.equals("2014") || digito4.equals("2149")) bandeira = "EN ROUTE";
			else bandeira = "INVALIDO";			
			break;
		  case 16:
			if (digito1.equals("4")) bandeira = "VISA";
			else if (digito2.compareTo("51") >= 0 && digito2.compareTo("55") <= 0) bandeira = "MASTERCARD";
			else bandeira = "INVALIDO";
			break;
		  case 0:
			bandeira = "INVALIDO";			
		  default:
			bandeira = "INVALIDO";
		}

        return bandeira;
    }
    
    public static boolean validaNumero(String numCartao) {
    	try {
    		int i, n = numCartao.length();
    		String[] cartao = new String[n];
    		for (i=0; i<numCartao.length(); i++) {
    			cartao[i] = "" + numCartao.charAt(i);
    		}
    		   		
    		int soma1, soma2;
    		soma1 = soma2 = 0;
    		
    		//Fase 1
    		for(i=numCartao.length()-1; i>=0; i-=2) {
    			soma1 += Integer.valueOf(cartao[i]);
    		}    		
    		//Fase 2
    		for(i=numCartao.length()-2; i>=0; i-=2) {
    			if( (Integer.valueOf(cartao[i])*2)<10 ) {
    				soma2 += (Integer.valueOf(cartao[i])*2);
    			}
    			else {
    				soma2 += ((Integer.valueOf(cartao[i])*2)-9);
    			}   			
    		}  		
    		//Fase 3
    		n = soma1 + soma2;
    		//Fase 4
    		return ((n%10 == 0));
    	}
    	catch (Exception e) 
    	{
            e.printStackTrace();
            return false;
    	}
    	
    }
		

}
