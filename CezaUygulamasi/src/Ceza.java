import javax.swing.JOptionPane;

public class Ceza {

    public static void main(String[] args) {
    	int hiz = 0;
    	int tekrar = 0;
    	
    	// hız 111 den küçük olamaz 
    	while (hiz < 111) {
    		String hizInput = JOptionPane.showInputDialog(null, "Hızı giriniz (km/sa): ");
    		hiz = Integer.parseInt(hizInput);
    		if (hiz < 111) {
    			JOptionPane.showMessageDialog(null, "HIZINIZ 111 DEN KÜÇÜK OLAMAZ", "Hatalı Giriş",
    					JOptionPane.ERROR_MESSAGE);
    		}
    	}
    	// tekrar e den küçük olamaz 
    	while (tekrar <= 0) {
    		String tekrarInput = JOptionPane.showInputDialog(null, "tekrar sayısı");
    		tekrar = Integer.parseInt(tekrarInput);
    		if (tekrar <= 0) {
    			JOptionPane.showMessageDialog(null, "tekrar 0 veya negatif olamaz", "Hatalı Giriş",
    					JOptionPane.ERROR_MESSAGE);
    		}
    	}
    	
        int bazCeza = 0;
        if (hiz >= 111 && hiz <= 140) {
            if (tekrar >= 1 && tekrar <= 3) {
                bazCeza = 150;
            } else if (tekrar >= 4 && tekrar <= 5) {
                bazCeza = 350;
            } else if (tekrar >= 6 && tekrar <= 8) {
                bazCeza = 800;
            } else {
                bazCeza = 5000;
            }
        } else if (hiz >= 141 && hiz <= 160) {
            if (tekrar >= 1 && tekrar <= 3) {
                bazCeza = 375;
            } else if (tekrar >= 4 && tekrar <= 5) {
                bazCeza = 875;
            } else if (tekrar >= 6 && tekrar <= 8) {
                bazCeza = 2000;
            } else {
                bazCeza = 11000;
            }
        } else if (hiz >= 161 && hiz <= 180) {
            if (tekrar >= 1 && tekrar <= 3) {
                bazCeza = 720;
            } else if (tekrar >= 4 && tekrar <= 5) {
                bazCeza = 1650;
            } else if (tekrar >= 6 && tekrar <= 8) {
                bazCeza = 3800;
            } else {
                bazCeza = 18000;
            }
        } else if (hiz >= 181) {
            if (tekrar >= 1 && tekrar <= 3) {
                bazCeza = 1200;
            } else if (tekrar >= 4 && tekrar <= 5) {
                bazCeza = 2800;
            } else if (tekrar >= 6 && tekrar <= 8) {
                bazCeza = 6500;
            } else {
                bazCeza = 42000;
            }
        }
        
        //baz cezayı bul
        String bazCezaMessage = "Baz Ceza: " + bazCeza + "TL";
        JOptionPane.showMessageDialog(null, bazCezaMessage, "Baz Ceza Miktarı", JOptionPane.ERROR_MESSAGE);
        
        int toplamCeza = bazCeza + hiz*2;
        
        //toplam cezayı bul
        String toplamCezaMessage = "Toplam Ceza: " + toplamCeza + "TL";
        JOptionPane.showMessageDialog(null, toplamCezaMessage, "Toplam Ceza Miktarı", JOptionPane.ERROR_MESSAGE);
    	

    }
}