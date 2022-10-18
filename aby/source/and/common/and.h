

#ifndef __BAND_H_
#define __BAND_H_

#include "../../../abycore/circuit/booleancircuits.h"
#include "../../../abycore/circuit/arithmeticcircuits.h"
#include "../../../abycore/circuit/circuit.h"
#include "../../../abycore/aby/abyparty.h"
#include "../../../abycore/sharing/sharing.h"
#include <math.h>
#include <cassert>


/**
 \param		role 		role played by the program which can be server or client part.
 \param 	address 	IP Address
 \param 	seclvl 		Security level
 \param 	nvals		Number of values
 \param 	bitlen		Bit length of the inputs
 \param 	nthreads	Number of threads
 \param		mt_alg		The algorithm for generation of multiplication triples
 \param 	sharing		Sharing type object
 \param 	num			the number of elements in the inner product
 \brief		This function is used for running a testing environment for solving the
 Inner Product.
 */
int32_t test_and_circuit(e_role role, char* address, uint16_t port, seclvl seclvl,
		uint32_t nvals, uint32_t bitlen, uint32_t nthreads, e_mt_gen_alg mt_alg,
		e_sharing sharing, uint32_t num);



share * BuildSharedAndCircuit(share *s_0, share *s_1,
                                BooleanCircuit *bc);

#endif
