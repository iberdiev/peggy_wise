from rest_framework import serializers
from . models import Category, PiggyBank

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name',)


class PiggyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiggyBank
        fields = ('category', 'limit', 'acummulating_rate', 'current_amount', 'total_amout', 'name')

'''

Everyday we spend money on the variety of things, food entertainment, shopping, traveling, etc,.
Usually, we always want to improve our spending habits by bying less, or buying what we actually need.
Piggy Bank is a feature in Wise application that helps to achieve exactly that. Save some money and improve our daily spending habits.
Wise have categories for the transactions made by the users, e.g. ....
For example, A customer wants to improve his/her spendings in one of the categories. Let's say food,
He creates a piggy bank instance in food category. He needs to determine transaction rate and limit.
Transaction rate is the percentage of the extra money to be transferred from the users account to the piggy bank from each tr at
corresponding category. These accumulated money are hidden from the user. At the end of each month, system will check
the spendings, and if the user spends more than the specified limit, he won't be able to withdraw that accumulated money,
and whenever user manages to spend less that the limit, those accumulated money will be available to take from the piggy bank.
With this feature, we provide an opportunity to improve spending habits of the users.


'''