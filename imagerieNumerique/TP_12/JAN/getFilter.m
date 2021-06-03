function H = getFilter(type,Img, D0, n)


m = max(size(Img)); 

P = 2^nextpow2(2*m);
PQ = [P, P];
M = P;
N = P;



u = 0:(M-1);
v = 0:(N-1);


idx = find(u > M/2);
u(idx) = u(idx) - M;
idy = find(v > N/2);
v(idy) = v(idy) - N;

[V, U] = meshgrid(v, u);

D = sqrt(U.^2 + V.^2);
figure
imshow(D);
title(' SEE D');


switch type
case 'ideal'
   H = double(D <=D0);
case 'butterworth'
   if nargin == 3
      n = 1;
   end
   H = 1./(1 + (D./D0).^(2*n));
case 'gaussian'
   H = exp(-(D.^2)./(2*(D0^2)));
end
end