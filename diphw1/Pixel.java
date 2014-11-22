import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.*;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import java.util.Scanner;

class Pixel {
    BufferedImage  image, bufferimage;
    int width;
    int height;
    int nw, nh, col;
    int [] standard;
    Scanner scan = new Scanner(System.in); 
    public Pixel() throws java.io.IOException {        
        File input = new File("img/91.png");
        image = ImageIO.read(input);
        width = image.getWidth();
        height = image.getHeight();
       
    }
    public void scaling() throws java.io.IOException {   
        System.out.println("Input the width and height: ");
        nw = scan.nextInt();//input the new width
        nh = scan.nextInt();//input the new height
        BufferedImage bufferimage = new BufferedImage(nw, nh, BufferedImage.TYPE_INT_RGB);
        for(int i=0; i<nh; i++){
            for(int j=0; j<nw; j++){               
                Color c = new Color(image.getRGB(j*width/nw, i*height/nh));//use proportional to scale up or down
                col =  (c.getRed() << 16) | (c.getGreen() << 8) | c.getBlue();
                bufferimage.setRGB(j, i, col);
            }
        }
        String str = "img/" + nw + "" + "_" + nh + "";
        ImageIO.write(bufferimage, "png", new File(str + ".png"));//wirte the image to the img folder
    } 



    public void quantize() throws java.io.IOException {
        BufferedImage bufferimage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        System.out.println("Input the level: ");
        int level = scan.nextInt();
        int standard[] = new int[level];
        int std = 255/(level - 1);
        double pix; 
        for(int i = 0; i < level; i++) {//get the standerd pixel first
            if(i != level - 1) {
                standard[i] = i*std;
            }
            else {
                standard[i] = 255;
            }
        }
        for(int i=0; i<height; i++){
            for(int j=0; j<width; j++){               
                Color c = new Color(image.getRGB(j, i));                          
                int outPixel;
                pix = c.getRed();
                //System.out.println(pix/std + " " + c.getRed()/std);               
                if(pix/std - c.getRed()/std <= 0.5) {
                    outPixel = standard[c.getRed()/std];
                }
                else {
                    if(c.getRed()/std + 1 < level)//this is for a possiable bug
                        outPixel = standard[c.getRed()/std + 1];
                    else
                        outPixel = 255;
                }
                //System.out.println(outPixel + " " + c.getRed());
                col =  (outPixel << 16) | (outPixel << 8) | outPixel;
                bufferimage.setRGB(j, i, col);
            }
        }
        String str = "img/" + level + "";
        ImageIO.write(bufferimage, "png", new File(str + ".png"));
    }
    
    static public void main(String args[]) throws Exception {
        Pixel obj = new Pixel();
        System.out.println("press 1 for scaling, 2 for quantizing");
        Scanner c = new Scanner(System.in);
        int choose = c.nextInt();
        if(choose == 1) {
             obj.scaling();
         }
         if(choose == 2) {            
             obj.quantize();
         }
    }
}

