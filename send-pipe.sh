
echo "hello " >/tmp/cmd_fifo
echo "ganesh " >/tmp/rsp_fifo
echo "bye " >/tmp/sur_fifo

sleep 2

value=10
for j in /tmp/cmd_fifo  /tmp/rsp_fifo /tmp/sur_fifo 
do
	echo $j
	for i in  {1..10}
	do
		((value=value+1))
		echo $value > $j
		sleep .01
	done
done

