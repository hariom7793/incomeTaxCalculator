# incomeTaxCalc.py
# - Gives taxable income and tax amount as per tax slab defined by indian gov for fy 2018-19
# Few assumptions have been made like person is resident and also as of now program is only for individual male
# Program will be upgraded in future to accommodate other features/option as well
# Program flow:
# 1. Takes input as few components from your salary structure
# 2. Calculates taxable income by removing exemption amounts
# 3. Calculates tax on taxable Income as per below formula:
#   tax = 0 * taxslab0 + 0.05 * taxslab1 + 0.2 * taxslab2 + 0.3 * abovetaxslab2
#

basicPay = int(input("Basic Pay : ")) * 12              # yearly
vpf = 0 * basicPay
hra = basicPay//2
convAllowance = 1600 * 12                               # yearly
spclAllowance = int(input("Special Allowance : ")) * 12 # yearly
lta = int(input("LTA : ")) * 12                         # yearly
medAllowance = 1250 * 12                                # yearly
exBonus = int(input("Ex-Gratia Bonus : ")) * 12         # yearly
varPay = int(input("Variable Pay : ")) * 4              # yearly
provFund = round(0.12 * basicPay,0)                     # yearly
profTax = 2500                                          # yearly, fix compo = 200 *11 + 300 = 1500

medReimbersement = int(input("Medical Reimbersement Amount : "))    #yearly

grossSal = basicPay + hra + convAllowance + spclAllowance + lta + medAllowance + exBonus + varPay

sec10Exemption = hra + lta + convAllowance + medReimbersement

incAfterExemption = grossSal - sec10Exemption
sec16Exemption = profTax

incAfterExemption -= sec16Exemption
chapVIdeduction = provFund

incAfterExemption -= chapVIdeduction
incAfterExemption -= vpf

taxableIncome = int(round(incAfterExemption/10,0)) * 10
savedTaxableIncome = taxableIncome - 250000
taxRate = 0


tax = 0
taxslab0, taxslab1, taxslab2, abovetaxslab2 = 0, 0, 0, 0

if taxableIncome >= 250000:
    taxslab0 = 250000
    taxableIncome -= taxslab0
    if taxableIncome >= 250000:
        taxslab1 = 250000
        taxableIncome -= taxslab1
        if taxableIncome >= 500000:
            taxslab2 = 500000
            taxableIncome -= taxslab2
            if taxableIncome > 0:
                abovetaxslab2 = taxableIncome
        else:
            taxslab2 = taxableIncome
    else:
        taxslab1 = taxableIncome
else:
    taxslab0 = taxableIncome

tax = 0 * taxslab0 + 0.05 * taxslab1 + 0.2 * taxslab2 + 0.3 * abovetaxslab2
educess = 0.03 * tax
payableTax = tax + educess

print("Total Income   : " + str(grossSal))
print("Taxable Income : " + str(savedTaxableIncome))
print("Tax            : " + str(tax))
print("Education Cess(3%): " + str(educess))
print("Total Tax Payable : " + str(payableTax))
print("Tax Payable p.m.  : " + str(payableTax/12))

