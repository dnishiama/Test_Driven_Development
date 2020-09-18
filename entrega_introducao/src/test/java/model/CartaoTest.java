package model;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import model.Cartao;

public class CartaoTest{
	
	Cartao card = new Cartao();
	String numero = "5256915663531845";
	
	@Test
	public void eNumero(){
		assertEquals (true, card.isNumber(numero));	
	}
	
	@Test
	public void validarBandeira(){	
		assertEquals ("MASTERCARD", card.validaBandeira(numero));	
	}
	
	@Test
	public void validarNumeroCartao(){		
		assertEquals (true, card.validaNumero(numero));	
	}
	
	@Test
	public void validarNumeroDigitos(){		
		assertEquals (true, card.validaDigitos(numero));	
	}
	
	
}