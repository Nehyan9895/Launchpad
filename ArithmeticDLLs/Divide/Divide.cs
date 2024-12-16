namespace Divide
{
    public class Division
    {
        public static int DivideNumbers(int a, int b)
        {
            if (b == 0)
                throw new DivideByZeroException("Cannot divide by zero.");
            return a / b;
        }
    }
}
