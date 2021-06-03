clear all;
close all;

lena = rgb2gray(im2double(imread('lena.png')));
std = 20;
V=(std/255)^2;
noisy_lena = imnoise(lena,'gaussian',0,V);

% a)
filter = ones(3,3) / 9;
denoisedImg2 = imfilter(noisy_lena,filter);

figure;

subplot(1,3,1);
imshow(lena);
title('Original ');

subplot(1,3,2);
imshow(noisy_lena);
title('Noisy ');

subplot(1,3,3);
imshow(denoisedImg2);
title(' time domain');

%  b)

 
Dideal = 250;
idealFilter = getFilter('ideal', noisy_lena, Dideal);



noisy_lena_Fourier=fft2(noisy_lena,size(idealFilter,1),size(idealFilter,2));
noisy = size(noisy_lena_Fourier)
ideal_noisy_lena_Fourier = idealFilter.*noisy_lena_Fourier;

ideal_noisy_lena=real(ifft2(ideal_noisy_lena_Fourier)); 

ideal_noisy_lena=ideal_noisy_lena(1:size(noisy_lena,1), 1:size(noisy_lena,2));
