namespace Add
{
    public class Addition
    {
        public static int AddNumbers(int a, int b)
        {
            if (a + b <= 1000)
            {
                return a + b;
            }
            else
            {
                throw new ArgumentOutOfRangeException("The sum of a and b exceeds 1000.");
            }
        }
    }
}
