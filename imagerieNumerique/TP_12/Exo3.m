clear all;
close all;
clc;

Img1 = rgb2gray(im2double(imread('img_001.jpeg')));
Img2 = im2double(imread('img_002.png'));
Img3 = im2double(imread('img_003.jpg'));
Img4 = im2double(imread('img_004.png'));

%Question a)----------------------------------------

%Bandreject ---------IDEAL-------------------------------

% WbtwBR = 20;
% DbtwBR = 250;
% btwBRF = Filter('ideal', Img1, DbtwBR,WbtwBR);
% btwFFTBR=fft2(Img1,size(btwBRF,1),size(btwBRF,2));
% btwBRImgFourier = btwBRF.*btwFFTBR;
% btwBRImgTime=real(ifft2(btwBRImgFourier));
% btwBRImgTime=btwBRImgTime(1:size(Img1,1), 1:size(Img1,2));
% 
% %Display
% subplot(2,2,1);imshow(Img1,[]);title('Original Image');
% subplot(2,2,2);imshow(btwBRImgTime, []);
% title('Filtered Image with ideal filter');
% subplot(2,2,3);imshow(log(1+abs(fftshift(btwFFTBR))),[]);
% title('Magnitude component');
% subplot(2,2,4);imshow(log(1+abs(fftshift(btwBRImgFourier))), []);
% title('Filterd magnitude with D =  & W =');


%Bandreject ---------GAUSSIAN-------------------------------

WgaussianBR = 250;
DgaussianBR = 300;
gaussianBRF = Filter('gaussian', Img1, DgaussianBR,WgaussianBR);
gaussianBRFFT=fft2(Img1,size(gaussianBRF,1),size(gaussianBRF,2));
gaussianImgFourierBR = gaussianBRF.*gaussianBRFFT;
gaussianImgTimeBR=real(ifft2(gaussianImgFourierBR));
gaussianImgTimeBR=gaussianImgTimeBR(1:size(Img1,1), 1:size(Img1,2));

%Display
figure;
subplot(2,2,1);imshow(Img1,[]);title('Original Image');
subplot(2,2,2);imshow(gaussianImgTimeBR, []);
title('Filtered Image with ideal filter');
subplot(2,2,3);imshow(log(1+abs(fftshift(gaussianBRFFT))),[]);
title('Magnitude component');
subplot(2,2,4);imshow(log(1+abs(fftshift(gaussianImgFourierBR))), []);
title('Filterd magnitude with D = 250 & W = 300');

%Bandreject ---------BUTTERWORTH-------------------------------

% WbtwBR = 50;
% DbtwBR = 450;
% btwBRF = Filter('butterworth', Img1, DbtwBR,WbtwBR);
% btwFFTBR=fft2(Img1,size(btwBRF,1),size(btwBRF,2));
% btwBRImgFourier = btwBRF.*btwFFTBR;
% btwBRImgTime=real(ifft2(btwBRImgFourier));
% btwBRImgTime=btwBRImgTime(1:size(Img1,1), 1:size(Img1,2));
% 
% %Display
% figure;
% subplot(2,2,1);imshow(Img1,[]);title('Original Image');
% subplot(2,2,2);imshow(btwBRImgTime, []);
% title('Filtered Image with ideal filter');
% subplot(2,2,3);imshow(log(1+abs(fftshift(btwFFTBR))),[]);
% title('Magnitude component');
% subplot(2,2,4);imshow(log(1+abs(fftshift(btwBRImgFourier))), []);
% title('Filterd magnitude with D =  & W =');
% 
% %******************************************************************
% %Bandpass ---------IDEAL-------------------------------
% 
% WidealBP = 150;
% DidealBP = 250;
% gaussianBPF = Filter('ideal', Img1, DidealBP,WidealBP);
% gaussianBPF = 1 - gaussianBPF;
% idealBPFFT=fft2(Img1,size(gaussianBPF,1),size(gaussianBPF,2));
% idealBPImgFourier = gaussianBPF.*idealBPFFT;
% idealBPImgTime=real(ifft2(idealBPImgFourier));
% idealBPImgTime=idealBPImgTime(1:size(Img1,1), 1:size(Img1,2));
% 
% %Display
% figure;
% subplot(2,2,1);imshow(Img1,[]);title('Original Image');
% subplot(2,2,2);imshow(idealBPImgTime, []);
% title('Filtered Image with ideal filter');
% subplot(2,2,3);imshow(log(1+abs(fftshift(idealBPFFT))),[]);
% title('Magnitude component');
% subplot(2,2,4);imshow(log(1+abs(fftshift(idealBPImgFourier))), []);
% title('Filterd magnitude with D =  & W =');


%Bandpass ---------GAUSSIAN-------------------------------

WgaussianBP = 200;
DgaussianBP = 50;
gaussianBPF = Filter('gaussian', Img1, DgaussianBP,WgaussianBP);
gaussianBPF = 1 - gaussianBPF;
gaussianBPFFT=fft2(Img1,size(gaussianBPF,1),size(gaussianBPF,2));
gaussianBPImgFourier = gaussianBPF.*gaussianBPFFT;
gaussianBPImgTime=real(ifft2(gaussianBPImgFourier));
gaussianBPImgTime=gaussianBPImgTime(1:size(Img1,1), 1:size(Img1,2));

%Display
figure;
subplot(2,2,1);imshow(Img1,[]);title('Original Image');
subplot(2,2,2);imshow(gaussianBPImgTime, []);
title('Filtered Image with ideal filter');
subplot(2,2,3);imshow(log(1+abs(fftshift(gaussianBPFFT))),[]);
title('Magnitude component');
subplot(2,2,4);imshow(log(1+abs(fftshift(gaussianBPImgFourier))), []);
title('Filterd magnitude with D = 200 & W = 50');

%Bandpass ---------BUTTERWORTH-------------------------------

% WbtwBP = 150;
% DbtwBP = 350;
% btwBPF = Filter('butterworth', Img1, DbtwBP,WbtwBP);
% btwBPF = 1 - btwBPF;
% btwBPFFT=fft2(Img1,size(btwBPF,1),size(btwBPF,2));
% btwBPImgFourier = btwBPF.*btwBPFFT;
% btwBPImgTime=real(ifft2(btwBPImgFourier));
% btwBPImgTime=btwBPImgTime(1:size(Img1,1), 1:size(Img1,2));
% 
% %Display
% figure;
% subplot(2,2,1);imshow(Img1,[]);title('Original Image');
% subplot(2,2,2);imshow(btwBPImgTime, []);
% title('Filtered Image with ideal filter');
% subplot(2,2,3);imshow(log(1+abs(fftshift(btwBPFFT))),[]);
% title('Magnitude component');
% subplot(2,2,4);imshow(log(1+abs(fftshift(btwBPImgFourier))), []);
% title('Filterd magnitude with D =  & W =');





