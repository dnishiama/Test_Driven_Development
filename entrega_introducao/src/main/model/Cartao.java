package model;

public class Cartao {
	public String numero;
	public String bandeira;

    private static final String[] bandeiras = {"Visa", "Mastercard", "American Express", "En Route", "Diner's CLub"};
    
    public static boolean isNumber(String n) {
        return false;
	}
    
    public static String validaBandeira(String numCartao) {
        String bandeira = "INVALIDO";
		return bandeira;
    }
    
    public static boolean validaNumero(String numCartao) {
    	return false;    	
    }

}
