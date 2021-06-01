
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

ideal_noisy_lena_Fourier = idealFilter.*noisy_lena_Fourier;

ideal_noisy_lena=real(ifft2(ideal_noisy_lena_Fourier)); 

ideal_noisy_lena=ideal_noisy_lena(1:size(noisy_lena,1), 1:size(noisy_lena,2));


%Butterworth low pass filter 

Dbutterworth = 300;
butterworthFilter = getFilter('butterworth', noisy_lena, Dbutterworth);
noisy_lena_Fourier2=fft2(noisy_lena,size(butterworthFilter,1),size(butterworthFilter,2));
butterworth_noisy_lena_Fourier = butterworthFilter.*noisy_lena_Fourier2;
butterworth_noisy_lena=real(ifft2(butterworth_noisy_lena_Fourier));
butterworth_noisy_lena=butterworth_noisy_lena(1:size(noisy_lena,1), 1:size(noisy_lena,2));

%Gaussian low pass filter 

Dgaussian = 250;
gaussianFilter = getFilter('gaussian', noisy_lena, Dgaussian);
noisy_lena_Fourier3=fft2(noisy_lena,size(gaussianFilter,1),size(gaussianFilter,2));
gaussian_noisy_lena_Fourier = gaussianFilter.*noisy_lena_Fourier3;
gaussian_noisy_lena=real(ifft2(gaussian_noisy_lena_Fourier));
gaussian_noisy_lena=gaussian_noisy_lena(1:size(noisy_lena,1), 1:size(noisy_lena,2));




figure; 
subplot(1,3,1);
imshow(lena, []);
title('Original Lenna');

subplot(1,3,2);
imshow(denoisedImg2);
title(' time domain');

subplot(1,3,3);
imshow(ideal_noisy_lena, []);
title(' ideal filter');

figure;

subplot(1,3,1);imshow(log(1+abs(fftshift(noisy_lena_Fourier))),[]);
title('Magnitude ');

subplot(1,3,2);imshow(log(1+abs(fftshift(ideal_noisy_lena_Fourier))), []);
title('Filterd magnitude ');

subplot(1,3,3);imshow(fftshift(idealFilter), []);
title('The ideal filter D0 = 250');


% Butterworth 

figure;
subplot(1,3,1);imshow(lena, []);title('Original ');
subplot(1,3,2);imshow(denoisedImg2);title(' time domain');
subplot(1,3,3);imshow(butterworth_noisy_lena, []);
title(' butterworth filter');

figure;

subplot(1,3,1);
imshow(log(1+abs(fftshift(noisy_lena_Fourier2))),[]);
title('Magnitude component ');

subplot(1,3,2);
imshow(log(1+abs(fftshift(butterworth_noisy_lena_Fourier))), []);
title('Filterd magnitude ');

subplot(1,3,3);
imshow(fftshift(butterworthFilter), []);
title('Butterworth filter D0 = 300');

% Gaussian results

% figure;
subplot(1,3,1);imshow(lena, []);title('Original ');
subplot(1,3,2);imshow(denoisedImg2);title(' time domain');
subplot(1,3,3);imshow(gaussian_noisy_lena, []);
title(' gaussian filter');

figure
% To visualize the magnitude component before and after being filtered
subplot(1,3,1);imshow(log(1+abs(fftshift(noisy_lena_Fourier3))),[]);
title('Magnitude ');
subplot(1,3,2);imshow(log(1+abs(fftshift(gaussian_noisy_lena_Fourier))), []);
title('Filterd magnitude ');
subplot(1,3,3);imshow(fftshift(gaussianFilter), []);
title('Gaussian filter D0 = 250');


%c)


MSEideal = immse(lena,ideal_noisy_lena);
MSEbutterworth = immse(lena,butterworth_noisy_lena);
MSEgaussian = immse(lena,gaussian_noisy_lena);
MSEnoisy = immse(lena,noisy_lena);
MSEtime = immse(lena,denoisedImg2);

