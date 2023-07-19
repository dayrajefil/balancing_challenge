class CustomerSuccessBalancing:
  def __init__(self, customer_success, customers, away_customer_success):
    self.customer_success = customer_success
    self.customers = customers
    self.away_customer_success = away_customer_success

  def execute(self):
    lowest_customer_score = min(self.customers, key=lambda customer: customer['score'])['score']
    self.customer_success = [success for success in self.customer_success if success['score'] >= lowest_customer_score]

    if self.away_customer_success:
      self.customer_success = [success for success in self.customer_success if success['id'] not in self.away_customer_success]

    if not self.customer_success:
      return 0

    sorted_customer_success = sorted(self.customer_success, key=lambda hash: hash['score'])

    services = {}

    for success in sorted_customer_success:
      services[success['id']] = 0

      self_customers_copy = self.customers.copy()

      for customer in self_customers_copy:
        if customer['score'] <= success['score']:
          services[success['id']] += 1
          self.customers.remove(customer)

    better_attendance = max(services.values())

    best_attendance_count = 0
    for key in services:
        if services[key] == better_attendance:
            best_attendance_count += 1

    if best_attendance_count > 1:
      result = 0
    else:
      for key, value in services.items():
        if value == better_attendance:
          result = key

    return result
