# coord-painter
Turn your painting to coordinate vectors.
input image | result coordinates
:----------:|:-----------------:
![input image](https://github.com/evanarlian/coord-painter/blob/main/images/input.png?raw=true) | ![result image](https://github.com/evanarlian/coord-painter/blob/main/images/result.png?raw=true) ![](https://...Ocean.png)

# Usage
1. Create any image, using paintbrush tool in mspaint is a good example.
2. The program will convert non-white pixels to coordinates.
	```
	python convert.py my_image.png
	```
3. Read the `.npy` files using NumPy.
4. The result may look flipped because `(0, 0)` coordinate in images are on the top left, but `(0, 0)` coordinate in plots are on the bottom left.

# Dependencies
PIL is used for reading and converting to RGB.  
NumPy is used for array manipulation. 
```
pip install Pillow
pip install numpy
```
The example uses matplotlib for plotting.
```
pip install matplotlib
```
