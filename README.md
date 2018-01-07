# ASCII_py-art
Generates ASCII Art output of the input image

### img.py
This Script Uses a set of *__ASCII characters__* to generate the ASCII ART Output.
	
Usage:
	python img.py [image] [output_type] [mode]

Parameters:  
	[image]         The input image file name for which ASCII art output is to be generated. Supports many formats.  
	[output_type]   An Integer Value.The type of output file/image.  
    	            	1 : 'image/jpg'  
        	        2 : 'image/png'  
            	    	3 : 'images/gif'  
                	4 : 'file/text'  
	[mode]          The Color Mode Of The Output image  
    	            	1 : 'L' ( Black-White / GrayScale )  
        	        2 : 'RGB' / Colored  
    	            	Note# : file/text supports only black-white  
  
Example:  
	python img.py images/wall.jpg 1 1  
		- This loads the image wall.jpg from the "images" directory.  
		   The Output generated will be an image of jpg type.  
		   And The Output generated will BlackWHite / GrayScaled.  
		   And The Output generated named 'wall_BW_art.jpg' will be stored in "output" directory.  

### img_uni.py
This Script Uses *__Unicode characters__* in a range mapped to normalized grayscale values to generate the ASCII ART Output.  
An improvement over the 'img.py' script  

Usage:  
	python img_uni.py [image] [output_type] [mode]  

Parameters:  
	[image]         The input image file name for which ASCII art output is to be generated. Supports many formats.  
	[output_type]   An Integer Value.The type of output file/image.  
					1 : 'image/jpg'  
					2 : 'image/png'  
					3 : 'images/gif'  
					4 : 'file/text'  
	[mode]          The Color Mode Of The Output image  
					1 : 'L' ( Black-White / GrayScale )  
					2 : 'RGB' / Colored  
					Note# : file/text supports only black-white  

Example:  
	python img_uni.py images/wall.jpg 1 2  
	 - This loads the image wall.jpg from the "images" directory.  
	   The Output generated will be an image of jpg type.  
	   And The Output generated will be Colored.  
	   And The Output generated named 'wall_RGB_uni_art.jpg' will be stored in "output" directory.  
