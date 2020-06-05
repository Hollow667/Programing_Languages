arr = [ 1, 2, 3, 4]
puts arr[0]

arr[1] = 3
print arr
puts arr

arr.each do |x| puts 2 * x end
 
puts arr.length

puts arr.first
puts arr.last

puts arr.first(3)
puts arr.last(3)

print arr.reverse

arr.push(5)
print arr
puts

arr.pop()
print arr
puts

arr.pop(4)
print arr

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = arr1 + arr2
print arr3
arr3 = arr3 - arr2
print arr3

puts "\n arr3 has 2" if arr3.include?(2)