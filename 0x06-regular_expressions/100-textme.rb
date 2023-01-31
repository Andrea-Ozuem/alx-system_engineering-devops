#!/usr/bin/env ruby
send = ARGV[0].scan(/\[from:(.+?)\]/)
to = ARGV[0].scan(/\[to:(.+?)\]/) 
puts ARGV[0].scan(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/).join(",")
