PROGRAM_NAME="lis.py"    # TODO: 請修改成你的執行檔名稱
PASSED=0
FAILED=0
TEST_DIR="./testcases"
ANS_FILE="./testcases/answers.txt"

COLOR_BRIGHT_BLUE="\033[36m"
COLOR_BLUE="\033[34m"
COLOR_RESET="\033[0m"
COLOR_GREEN="\033[32m"
COLOR_RED="\033[31m"
COLOR_YELLOW="\033[33m"

clear

for test_file in $TEST_DIR/*.lsp; do
    test_name=$(basename $test_file)

    echo "$test_name"
    expected_output=$(awk "/^$test_name$/{flag=1;next}/^[a-zA-Z0-9]+_[0-9]+\.lsp$/{flag=0}flag" "$ANS_FILE")
    actual_output=$(python $PROGRAM_NAME < $test_file 2>&1)

    expected_output=$(echo "$expected_output" | tr -d '\r')
    actual_output=$(echo "$actual_output" | tr -d '\r')

    echo -e "\033[36mTest: $test_name\033[0m"

    if [ "$expected_output" == "$actual_output" ]; then
        echo -e "\033[32mResult: PASS\033[0m"
        ((PASSED++))
    else
        echo -e "${COLOR_RED}Result: FAIL${COLOR_RESET}"
        echo "Expected Output:"
        echo -e "${COLOR_RED}$expected_output${COLOR_RESET}"
        echo "Actual Output:"
        echo -e "${COLOR_RED}$actual_output${COLOR_RESET}"
        ((FAILED++))
    fi

    echo -e "\033[35m-----------------------------------\033[0m"
done

echo -e "${COLOR_YELLOW}Tests completed.${COLOR_RESET} ${COLOR_GREEN}Passed: $PASSED${COLOR_RESET}, ${COLOR_RED}Failed: $FAILED${COLOR_RESET}"