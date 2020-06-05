dic = {"key1" => "val1", "key2" => "val2"}

puts dic.size
puts dic['key1']

dic['key1'] = 'nval1'
dic['key3'] = 'val3'

dic.each do |key, val| puts key + ":" +val end

puts dic.keys

dic.delete('key3')

print dic
