import random


certs = {"eur" : 0,
         "usd" : 0,
         "jpy" : 0,
         "chf" : 0,
         "gbp" : 0,
         "cad" : 0,
         "cny" : 0,
}


options = {0 : "eur",
           1 : "usd",
           2 : "jpy",
           3 : "chf",
           4 : "gbp",
           5 : "cad",
           6 : "cny",
}


def increase_cert_nb(currency):
	certs[currency] += 1


def write_result():
	res = "Starting Certificates: "
	for key, value in certs.items():
		if value == 0:
			continue
		res += "{0} {1}, ".format(value, key.upper())
	return res[:-2]

def draw_certs():
	global certs
	certs = dict.fromkeys(certs.iterkeys(), 0)
	for _ in xrange(6):
		r = random.randint(0, 6)
		increase_cert_nb(options[r])
	return write_result()