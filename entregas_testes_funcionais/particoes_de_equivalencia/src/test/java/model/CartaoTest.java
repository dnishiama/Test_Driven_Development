package model;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import model.Cartao;

public class CartaoTest{
	
	Cartao card = new Cartao();

	/** Testes de partição:
	*
	* Teste isNumber possui 2 partições: 
	*	Entrada de numeros ou caracteres
	*
	* Teste digitos possui 3 partições: 
	*	Cartões com digitos ...> 13~16 <... 
	*
	* Teste luhn possui 2 partições
	* 	Algoritmo de Luhn: processo matemático cujo resultado deve ser divisível por 10. 
	*	Valida ou Invalida
	*
	* Partição validaBandeira possui um conjunto de partições:
	* 	
	*	Caso especial cartões que possui ou podem possuir mesmo numero de digitos ou seja o inferior de um contempla o superior do outro:
	*	Visa: o 1º digito é 4: 3 partições.
	* 	Mastercard: os 2 primeiros digitos são 51 à 55: 3 partições.
	*
	*	Caso especial cartões que possui ou podem possuir mesmo numero de digitos ou seja o inferior de um contempla o superior do outro:
	* 	American Express: os 2 primeiros digitos são 34 ou 37: 5 partições.
	* 	En Route: os 4 primeiros digitos são 2014 ou 2019: 4 partições.
	*
	* 	Diners Club: os 2 primeiros digitos são 36 ou 38 ou os 3 primeiros digitos são 300 à 305: 7 partições.
	*
	* 	Soma: 21 partições 
	*	Subtrai: 2 partiçoes contempladas nas situações especiais.
	*	Total 20 partições.
	*
	* Para os testes True, foi gerado numeros no site: https://www.4devs.com.br/gerador_de_numero_cartao_credito
	**/
	
	@Test
	public void isNumberTrue(){ assertEquals (true, card.isNumber("5256915663531845"));	}	
	@Test
	public void isNumberFalse(){ assertEquals (false, card.isNumber("525691566353184a")); }

	@Test
	public void luhnTrue(){ assertEquals (true, card.validaNumero("5256915663531845")); }
	@Test
	public void luhnFalse(){ assertEquals (false, card.validaNumero("525691566353184")); }
	
	@Test
	public void digitosTrue(){ assertEquals (true, card.numDigitos("5256915663531845")); }
	@Test
	public void digitosFalseInferior(){ assertEquals (false, card.numDigitos("525691566353"));	}
	@Test 
	public void digitosFalseSuperior(){ assertEquals (false, card.numDigitos("52569156635318465")); }
	
	@Test 
	public void masterTrue(){ assertEquals ("MASTERCARD", card.validaBandeira("5190826423094355"));}
	@Test
	public void masterFalseSuperior(){ assertEquals ("INVALIDO", card.validaBandeira("5690826423094355")); }
	
	@Test 
	public void visaTrue(){ assertEquals ("VISA", card.validaBandeira("4532905292826111"));}
	@Test
	public void visaFalseInferior(){ assertEquals ("INVALIDO", card.validaBandeira("0532905292826111")); }
	@Test
	public void visaFalseSuperiorMasterInferior(){ assertEquals ("INVALIDO", card.validaBandeira("5032905292826111")); }
	
	@Test 
	public void amexTrue34(){ assertEquals ("AMERICAN EXPRESS", card.validaBandeira("340587625894733"));}
	@Test 
	public void amexTrue37(){ assertEquals ("AMERICAN EXPRESS", card.validaBandeira("372602838014952"));}
	@Test
	public void amexFalseInferior(){ assertEquals ("INVALIDO", card.validaBandeira("332602838014952")); }
	@Test
	public void amexFalseMiddle(){ assertEquals ("INVALIDO", card.validaBandeira("352602838014952")); }
	@Test
	public void amexFalseSuperiorEnRouteInferior(){ assertEquals ("INVALIDO", card.validaBandeira("392602838014952")); }
		
	@Test 
	public void enRouteTrue2014(){ assertEquals ("EN ROUTE", card.validaBandeira("201455777256291"));}
	@Test 
	public void enRouteTrue37(){ assertEquals ("EN ROUTE", card.validaBandeira("214993200601092"));}
	@Test
	public void enRouteFalseMiddle(){ assertEquals ("INVALIDO", card.validaBandeira("200093200601092")); }
	@Test
	public void enRouteFalseSuperior(){ assertEquals ("INVALIDO", card.validaBandeira("215093200601092")); }
			
	@Test 
	public void dinersTrue36(){ assertEquals ("DINERS CLUB", card.validaBandeira("36933036493765"));}
	@Test 
	public void dinersTrue38(){ assertEquals ("DINERS CLUB", card.validaBandeira("38195120047034"));}
	@Test 
	public void dinersTrue300(){ assertEquals ("DINERS CLUB", card.validaBandeira("30039451301149"));}
	@Test
	public void dinersFalseInferior(){ assertEquals ("INVALIDO", card.validaBandeira("35933036493765")); }
	@Test
	public void dinersFalseBetween36and38(){ assertEquals ("INVALIDO", card.validaBandeira("37195120047034")); }
	@Test
	public void dinersFalseMiddle(){ assertEquals ("INVALIDO", card.validaBandeira("29939451301149")); }
	@Test
	public void dinersFalseSuperior(){ assertEquals ("INVALIDO", card.validaBandeira("30639451301149")); }
}