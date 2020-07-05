using NUnit.Framework;

namespace Calc.Tests
{
    public class Tests
    {
        void TestReshenie(double x, double y, double[] exResult)
        {
            var result = CodeCalculator.Calc(x, y);

            Assert.AreEqual(exResult.Length, result.Length);

            for (int i = 0; i < result.Length; i++)
                Assert.AreEqual(exResult[i], result[i]);
        }
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void FuncionCalc()
        {
            TestReshenie(10, 5, new double[] { 15, 5, 50, 2 });
        }

        [Test]
        public void DivisionOnZero()
        {
            TestReshenie(5, 0, new double[] { 0 });
        }
    }
}