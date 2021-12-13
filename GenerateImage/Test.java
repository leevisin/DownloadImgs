import javax.imageio.ImageIO;
import javax.imageio.stream.ImageOutputStream;
import java.awt.image.BufferedImage;
import java.io.*;

public class Test {

    public static void main(String[] args) throws IOException {
        try{
            /* 读入TXT文件 */
            String pathname = "D:\\IdeaProject\\GenerateImgs\\src\\Test.txt"; // 绝对路径或相对路径都可以，这里是绝对路径，写入文件时演示相对路径
            File filename = new File(pathname); // 要读取以上路径的input.txt文件
            InputStreamReader reader = new InputStreamReader(
                    new FileInputStream(filename)); // 建立一个输入流对象reader
            BufferedReader br = new BufferedReader(reader); // 建立一个对象，它把文件内容转成计算机能读懂的语言
            String line = "";
            line = br.readLine();
            int i=0;
            while (line != null) {
                line = br.readLine(); // 一次读入一行数据
                String[] splitedString = line.split("\t");
//                System.out.println("splitedString[0] = "+ splitedString[0]);
//                System.out.println("splitedString[1] = "+ splitedString[1]);
                if (i == 10) {
                    break;
                }
                String[] firString = new String[1];
                String[] secString = new String[1];
                firString[0] = splitedString[0];
                secString[0] = splitedString[1];
                generateImg(firString, i++);
                generateImg(secString, i++);
            }

            System.out.println(i);
        } catch (Exception e) {
            System.out.println("Enter Exception");
        }
    }

    public static void generateImg(String[] fileString, int fileNum) throws IOException {
        BufferedImage image = CommonUtil.createImage(fileString);
        File file = new File("D:/IdeaProject/GenerateImgs/NewTest");
        String fileName = "word_" + fileNum + ".jpg";
        File jpgFile = new File(file,fileName);
        if(!jpgFile.exists()) {
            jpgFile.createNewFile();
        }
        // 创建图片输出流对象，基于文件对象
        ImageOutputStream imageOutputStream = ImageIO.createImageOutputStream(jpgFile);
        // 写入
        ImageIO.write(image,"jpg",imageOutputStream);
        // 关闭流
        imageOutputStream.close();

        File writename = new File(".\\train.txt"); // 相对路径，如果没有则要建立一个新的output。txt文件
        writename.createNewFile(); // 创建新文件
        BufferedWriter out = new BufferedWriter(new FileWriter(writename, true));
        out.write("train/word_"+ fileNum +".jpg\t"+ fileString[0] +"\r\n"); // \r\n即为换行
        out.flush(); // 把缓存区内容压入文件
        out.close(); // 最后记得关闭文件
    }
}
