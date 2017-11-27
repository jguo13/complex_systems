%% A 1-D Random Walk
%produces an 8 x 1000 array of steps, where each step is either -1 or +1
walk=round(rand(8,1000))*2-1
%creates an array of locations
locations= cumsum(walk,1) 
figure(1)
clf;
plot(locations(:, 1:6));
xlabel('Number of Steps');
ylabel('Location')

%% B Statistics
%creates a 1x1000 array of the final location of each track
final_locations= locations(8, :); 
%mean location is 0
disp(mean2(final_locations))
%variance is 8
disp(var(final_locations))
%theoretical value is 0, since there is a 50% probabilty of -1 and 50%
%probability of 1
disp(.5.*1+.5*-1)
%creats bins knowing that locations are even
bins = -9:2:9;
%histogram of final locations
histogram(final_locations,bins, 'normalization', 'pdf')
hold all
%calculate bin centers
bin_centers = 0.5*(bins(1:9)+bins(2:10));
%binomial=factorial(8)./factorial(k).*factorial(8-k).*.5^(8)
k = 0:1:8;
binomial=(factorial(8)./(factorial(k).*factorial(8-k)).*.5^(8))./2
plot(bin_centers,binomial,'ko-')
%% 5th Problem
%creates a new array of 200 x values with finer spacing
x=linspace(-9,9,200)
%y values for the normal distribution
normal = 1./(sqrt(8).*sqrt(2*pi))*exp(-(x - 0).^2./(2*8))
plot(x,normal, 'r-')
xlabel('Number of Steps');
ylabel('Final Location')
legend('Random Walk Generator','normal distribution','binomial distribution')
title('One Dimensional Random Walk')

%% 7th Problem
%Figure for first 6 tracks
%produces an 8 x 2000 array of steps, where each step is either -1 or +1
walk=round(rand(1000,2000))*2-1
%creates an array of locations
locations= cumsum(walk,1) 
figure(1)
clf;
plot(locations(:, 1:6));
xlabel('Number of Steps');
ylabel('Location')

%histogram for end results
%creates a 1x1000 array of the final location of each track
final_locations= locations(1000, :); 
%mean location is 0
disp(mean2(final_locations))
%variance is 8
disp(var(final_locations))
%theoretical value is 0, since there is a 50% probabilty of -1 and 50%
%probability of 1
disp(.5.*1+.5*-1)
%creats bins knowing that locations are even
bins = -1001:2:1001;
%histogram of final locations
histogram(final_locations,bins, 'normalization', 'pdf')
hold all
%normal distribution
%creates a new array of 200 x values with finer spacing
x=linspace(-1001,1001,200)
%y values for the normal distribution
normal = 1./(sqrt(1000).*sqrt(2*pi))*exp(-(x - 0).^2./(2*1000))
plot(x,normal, 'r-')
xlabel('Number of Steps');
ylabel('Final Location')
legend('Random Walk Generator','normal distribution')
title('One Dimensional Random Walk')