document.addEventListener('DOMContentLoaded', function() {
    const display = document.getElementById('display');
    const buttons = Array.from(document.querySelectorAll('.btn'));

    let currentInput = '';
    let previousInput = '';
    let operator = '';

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const value = button.getAttribute('data-value');

            switch(value) {
                case 'C':
                    currentInput = '';
                    previousInput = '';
                    operator = '';
                    display.textContent = '0';
                    break;
                case '=':
                    if (operator && previousInput) {
                        currentInput = evaluate(previousInput, currentInput, operator);
                        display.textContent = currentInput;
                        previousInput = '';
                        operator = '';
                    }
                    break;
                case '+':
                case '-':
                case '*':
                case '/':
                    if (currentInput) {
                        if (previousInput) {
                            previousInput = evaluate(previousInput, currentInput, operator);
                            display.textContent = previousInput;
                        } else {
                            previousInput = currentInput;
                        }
                        currentInput = '';
                        operator = value;
                    }
                    break;
                default:
                    currentInput += value;
                    display.textContent = currentInput;
            }
        });
    });

    function evaluate(a, b, operator) {
        const numA = parseFloat(a);
        const numB = parseFloat(b);
        switch(operator) {
            case '+':
                return (numA + numB).toString();
            case '-':
                return (numA - numB).toString();
            case '*':
                return (numA * numB).toString();
            case '/':
                return (numA / numB).toString();
        }
    }
});