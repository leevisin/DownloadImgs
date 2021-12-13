# Download Image
Download images from url that likes http://avatar.csdn.net/1/3/B/1_li1325169021.jpg

Thanks for 小光Y, he/she's code can run correctly. And it reduces the duplicate operations. 
You can use for loop to download database that can read from web like the link above simply.

>[java根据图片路径下载图片并保存到本地目录](https://www.cnblogs.com/xiaoguangy/p/11497700.html)


# Generate Image
Generate images by Strings read data from txt file

CommonUtil.java class is the util to control image's style, such as background's length and height, font style, font color, etc.

Test.java class is to generate images, pathname should be changed accordingly, I have no idea about relative pathname, 
so please change to absolute pathname if you have no idea.

In Test class, it reads one line each. There are two items in one line and seperate by '\t'(i.e tab), you can change them according to your txt file.
