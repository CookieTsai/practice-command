
function myfunc1() {
    sleep 1
    echo "I'm work $1"
    sleep 5
    echo "I'm done $1"
}

echo "start"

for i in `seq 1 10`; do
    myfunc1 $i &
done

wait

echo "End"
