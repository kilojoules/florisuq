clc; clear all; close all

data = load('tmp.dat');

u_inf = 10 ;
rho_inf = 1.177
qinf = 0.5 * rho_inf * u_inf * u_inf ;
AOA = ANGLE ;

cx = data(:,2) + data(:,5);
cy = data(:,3) + data(:,6);

cd = cosd(AOA).*cx + sind(AOA).*cy;
cl = -sind(AOA).*cx + cosd(AOA).*cy;

cd = cd./qinf * 1e4;
cl = cl./qinf;

fid = fopen('forces.dat','w');

for i = 1:length(cl)

fprintf(fid,'%12.9f %12.9f %12.9f\n',[data(i,1) cd(i) cl(i)]);

end

fclose(fid)
