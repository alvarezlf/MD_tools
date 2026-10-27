if [ $# -ne 3 ]; then
    echo "Usage: $0 <N_atoms> <step_number> <trajectory_file.xyz>"
    exit 1
fi

N=$2
S=$3
traj_file=$1

frame_size=$((N + 2))
final_line=$((frame_size * (S + 1)))
head -n "$final_line" "$traj_file" | tail -n "$frame_size"


