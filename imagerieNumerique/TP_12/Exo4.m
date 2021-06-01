clc;
clear all;
close all;

Img5 = im2double(imread('img_005.jpg'));
Img6 = rgb2gray(im2double(imread('img_006.jpg')));

%a)
w1 = 7;
denoisedT_Img5 = medfilt3(Img5,[w1 w1 3]);

figure;
subplot(121); imshow(Img5);
title('Original image');
subplot(122); imshow(denoisedT_Img5);
title('Denoised image in time domain with N = 7');

% b)

D = 50;
W = 200;
Filter = Filter('gaussian', Img5, D,W);

noisy_Fourier=fft2(Img5,size(Filter,1),size(Filter,2));

Filter = 1 - Filter;

filtered_noisy_Fourier = Filter.*noisy_Fourier;

filtered_noisy=real(ifft2(filtered_noisy_Fourier)); 

filtered_noisy=filtered_noisy(1:size(Img5,1), 1:size(Img5,2));

% Dgaussian = 3;
% 
% enhanced_lena = GaussianHighpass(Img5,Dgaussian);
% figure;
% subplot(133);imshow(enhanced_lena);
% title('Enhanced image with gaussian highpass filter, D0 = 3');
% subplot(1,3,2);imshow(denoisedT_Img5);
% title('Denoised image in time domain');
% subplot(1,3,1);imshow(Img5, []);
% title('Original image');



figure; 
subplot(1,3,1);imshow(Img5, []);title('Original image');
subplot(1,3,2);imshow(denoisedT_Img5);title('Denoised image in time domain');
subplot(1,3,3);imshow(filtered_noisy, []);
title('Denoised image with gaussian Bandpass, D0 = 100, W = 400');

 figure;
% To visualize the magnitude component before and after being filtered
imshow(log(1+abs(fftshift(noisy_Fourier))),[]);
title('Magnitud component of the image');
