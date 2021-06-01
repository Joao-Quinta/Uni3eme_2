function H = Filter(type, Img, D0,W,n)

mideal = max(size(Img)); 

P = 2^nextpow2(2*mideal);
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


switch type
case 'ideal'
   H = not(double((D >= (D0-(W/2))) & (D <= (D0+(W/2)))));
case 'butterworth'
   if nargin == 4
      n = 1;
   end
   H = 1./(1 + ((D.*W)./((D.^2)-(D0^2))).^(2*n));
case 'gaussian'
   H = 1-exp(-(((D.^2)- D0^2)./((D.*W))).^2);
end
end