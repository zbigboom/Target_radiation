function[B_i,M_i,N]=fun1(c1,c2,F1,F2,T,At)
%  c1 = 3.7415e4;%第一辐射常数
%  c2 = 1.438789e4;%第二辐射常数
%  F1=3;
%  F2=5;
%  T=900;
%  At=1;
 i=1;
 N=[F1:0.01:F2];
 L=length(N);
 M_i=zeros(1,L);
 B_i=zeros(1,L);
for F=F1:0.01:F2
    M=(c1./(F.^5)./(exp(c2./(F.*T))-1)); 
    M_i(1,i)=M;
    B=M*At;
    B_i(1,i)=B;
    i=i+1;
end  
figure(1)
plot(N,M_i)
figure(2)
plot(N,B_i)
 end