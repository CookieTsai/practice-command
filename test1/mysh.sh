
function myfunc1() {
    echo "I'm work"
    sleep 10
    echo "I'm done"
}

echo "start"

myfunc1 &
sleep 1

myfunc1 &
sleep 1

myfunc1 &

wait

echo "End"
