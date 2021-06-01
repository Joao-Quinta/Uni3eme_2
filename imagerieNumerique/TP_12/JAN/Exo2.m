clc;
clear all;
close all;

lena = rgb2gray(im2double(imread('lena.png')));

filterSize = 3;
blurry_lena = imboxfilt(lena,filterSize);


% a)

h = fspecial('gaussian',5,3);
sharped_lena = filter2(h,blurry_lena);
k = 1;
u = blurry_lena - sharped_lena;
sharped_lena = blurry_lena + k*u;

figure;
subplot(131);
imshow(lena);
title('Original ');

subplot(132);
imshow(blurry_lena);
title('Blurry Lenna');

subplot(133);
imshow(sharped_lena);
title(' time domain');

% b)

D0 = 10;



[m,n]=size(blurry_lena);
Img_Fourier=fft2(blurry_lena);
f_shift=fftshift(Img_Fourier);
p=m/2;
q=n/2;

for i=1:m
    for j=1:n
        distance=sqrt((i-p)^2+(j-q)^2);
        
        high_filter(i,j)=1-exp(-(distance)^2/(2*(D0^2)));
    end
end

figure;
imshow(high_filter);
title('Gaussian highpass filter with D0 = 10');
filter_apply=f_shift.*high_filter;
image_orignal=ifftshift(filter_apply);
image_filter_apply2=real(ifft2(image_orignal));
enhanced_lena = image_filter_apply2;

figure;
subplot(133);imshow(enhanced_lena);
title(' gaussian highpass filter');
subplot(132);imshow(blurry_lena);
title('Blurry ');
subplot(131);imshow(sharped_lena);
title('  time domain');


%ideal
figure;

[M, N] = size(blurry_lena);
  

FT_img = fft2(double(blurry_lena));
  

D0 = 10; 
  

u = 0:(M-1);
idx = find(u>M/2);
u(idx) = u(idx)-M;
v = 0:(N-1);
idy = find(v>N/2);
v(idy) = v(idy)-N;
  

[V, U] = meshgrid(v, u);
  
D = sqrt(U.^2+V.^2);
  

H = double(D > D0);
  
G = H.*FT_img;
imshow(G);
figure;
   
output_image = real(ifft2(double(G)));
  
% Displaying Input Image and Output Image
subplot(1, 2,1), imshow(blurry_lena);
title('blurry lena');
subplot(1, 2,2), imshow(output_image, [ ]);
title('idéal d = 10');




