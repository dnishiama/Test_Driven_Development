package model;

public class Cartao {
	public String numero;
	public String bandeira;

    private static final String[] bandeiras = {"Visa", "Mastercard", "American Express", "En Route", "Diner's CLub"};
    
    public static int isNumber(String n) {
        return 0;
    }	
		
	public static int numDigitos(String numCartao){
		return 0;
	}
    
    public static String validaBandeira(String numCartao) {
        String bandeira = "INVALID";
        return bandeira;
    }
    
    public static int validaNumero(String numCartao) {
        return 0;
    }		

}