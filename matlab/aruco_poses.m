

R0 = [ 0  0 -1;
     -1  0  0;
      0  1  0];

q0 = [1 0 0 0];
q0 = rotm2quat(R0);


H_c_r = eye(4);
H_c_r(1:3,1:3) = [ 0  0  1;
                  -1  0  0;
                   0 -1  0];
H_c_r(1:3,4) = [0.2; 0; 0];


H1 = H_from_pq([3 2.12 0.11], q0);
H2 = H_from_pq([5 0.12 0.11], q0);
H3 = H_from_pq([7 2.12 0.11], q0);
H4 = H_from_pq([9 0.12 0.11], q0);
H5 = H_from_pq([11 2.12 0.11], q0);
H6 = H_from_pq([13 0.12 0.11], q0);
H7 = H_from_pq([15 2.12 0.11], q0);
H8 = H_from_pq([17 0.12 0.11], q0);
H9 = H_from_pq([19 2.12 0.11], q0);
H10 = H_from_pq([21 0.12 0.11], q0);
H11 = H_from_pq([23 2.12 0.11], q0);
H12 = H_from_pq([25 0.12 0.11], q0);

H = [];
for k = 1:1:12
    eval(sprintf('H(:,:,k) = H%d',k));
end


plot3(0,0,0,'k.')
hold on
plot_frame(eye(4),1,5);
axis equal
grid on

for k = 1:1:12
    plot_frame(H(:,:,k),1,2);
end
hold off



for k = 1:1:12
    
    fprintf(sprintf('H%d = np.matrix([[%f,%f,%f,%f],[%f,%f,%f,%f],[%f,%f,%f,%f],[0.0,0.0,0.0,1.0]])\n',k,H(1,1,k),H(1,2,k),H(1,3,k),H(1,4,k),H(2,1,k),H(2,2,k),H(2,3,k),H(2,4,k),H(3,1,k),H(3,2,k),H(3,3,k),H(3,4,k)));
    fprintf(sprintf('H_a_w_list.append(H%d)\n',k));
    
end











