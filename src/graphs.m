syms v H M
%a(H) = 340.28431 - 0.00382 * H;
%M(v, H) = v / a(H);
engines = 3;
P(M) = engines * (112/33 * M * M - 1142/165 * M + 18387/550) * 1000;
%rho(h)

Cy0=-0.221;
Cyalpha=0.082;
%Cy = @(alpha) Cyalpha * alpha + Cy0;

M1 = 0.2;
M2 = 0.9;
MM = M1:(M2-M1)/100:M2;
PP = P(MM);

aa = 10:0.1:20;
CyCy = Cy(aa);
CxCx = Cx(aa);

figure(1)
plot(MM, PP)
grid on
grid minor
title("Тяга")
xlabel('M') 
ylabel('P, H') 
figure(2)
plot(aa, CxCx)
title("Cx")
xlabel(['\alpha, ' char(176)]) 
ylabel('Cx') 
grid on
figure(3)
plot(aa, CyCy)
title("Cy")
xlabel(['\alpha, ' char(176)]) 
ylabel('Cy') 
grid on

function Cy_f = Cy(alpha)
    Cy0=-0.221;
    Cyalpha=0.082;
    Cy_f = Cyalpha * alpha + Cy0;
end

function Cx_f = Cx(alpha)
    cy_a = Cy(alpha);
    Cx_f = 0.128 * cy_a .* cy_a - 0.072 * cy_a + 0.032;
end