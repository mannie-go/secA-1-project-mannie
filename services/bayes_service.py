def calculate_bayes(prior, likelihood, evidence): #สร้างฟังก์ชันสำหรับคำนวณ Bayes
   if prior < 0 or prior > 1: #รับค่า Prior Probability
       raise ValueError("Prior must be between 0 and 1")
   if likelihood < 0 or likelihood > 1: #รับค่า likelihiid
       raise ValueError("Likelihood must be between 0 and 1")
   if evidence <= 0 or evidence > 1: #รับค่า Evidence
       raise ValueError("Evidence must be greater than 0 and not more than 1")
   posterior = (prior * likelihood) / evidence
   if posterior > 1: #ตรวจสอบว่าค่าความน่าจะเป็นอยู่ในช่วงที่ถูกต้อง
       raise ValueError("Invalid probability values") #posterior นำค่าทั้งสามมาคำนวณตามสูตร
   return posterior #ส่งผลลัพธ์กลับไปให้หน้าเว็บ