#!/usr/bin/env ruby

def parse_log(log)

  regex1 = /\bfrom:\s*([\w._%+-]{2,})\b/
  regex2 = /\+\d{11}/ 
  regex3 = /\d{11}/
  regex4 = /\bto:\s*([\w._%+-]{2,})\b/
  regex5 = /(?:-1|0)(?::(?:-1|0))*/

  match1 = log.match(regex1)
  match2 = log.match(regex2)
  match3 = log.match(regex3)
  match4 = log.match(regex4)
  match5 = log.match(regex5)

  sender = nil
  receiver = nil
  flags = nil

  if match4 then
   receiver = match4[1]
  end

  if match1 then
    sender = match1[1]
  elsif match2 then
    sender = match2[1]
    receiver = match2[2]
  elsif match3 then
    sender = match3[1]
    receiver = match3[2]
  else
    return "Invalid input"
  end

  if match5 then
    flag = match5[1]
  end
  return "#{sender},#{receiver},#{flag}"
end
