package exhalia;

import java.awt.Toolkit;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.sql.Date;
import java.text.SimpleDateFormat;

public class SimpleHTTPServer {
	private static String decode(String value) {
	    try {
			return URLDecoder.decode(value, StandardCharsets.UTF_8.toString());
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
			return "";
		}
	}

    public static void main(String args[]) throws Exception {

        final ServerSocket server = new ServerSocket(4000);
        CScentDiffusionContext diffusionContext = new CScentDiffusionContext("","SCENT_4","","","10","10","");
        int count;
        String command;

        System.out.println("Listening for connection on port 4000 ....");
        while (true) {

            final Socket client = server.accept(); // Accepting connection
            InputStreamReader isr = new InputStreamReader(client.getInputStream());
            BufferedReader reader = new BufferedReader(isr);
            count =0;
            String line = reader.readLine();
            while (!line.isEmpty()) {
            	if(count == 0){
            		command = decode(line);
            		try{
            		command = command.substring(command.indexOf(","), command.lastIndexOf(",")+1);}
            		catch (StringIndexOutOfBoundsException e){
            			System.out.print(e);
            		}
            		System.out.println(command);
            		diffusionContext.DiffuseCommand(command);
                }
                line = reader.readLine();
                
                //",SCENT_3,,,10,10,"
                
                count++;
            }

            // print number of request, date and time 
            long time = (System.currentTimeMillis());
            System.out.println(time);
            
        }
    }
}
