arr = ["data1", "data2", "data3"]
arr[0] = "datam1"
puts arr     #all array#
puts arr[0]  #first element#
puts arr[-1] #last element#

#multi type items#
arr2 = [1,1.2,"str"]
puts arr2

#iterate#
arr3 = ["data1", "data2", "data3"]
for item in arr3
  puts item
end

for item in arr3.reverse
  puts item
end

arr3.each do |item|
  puts item
end

arr3.each_with_index do |item, index|
  puts index
  puts item
end
