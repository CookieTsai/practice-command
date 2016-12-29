func1 () { 
    sleep $1; 
    echo 1; 
}

func1 2 &
func1 4 &
func1 3 &

wait


