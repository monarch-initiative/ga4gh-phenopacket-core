import io
import os

import pytest

from ppsc.parse.json import JsonSerializer, JsonDeserializer
from ppsc.v202 import *


class TestJsonSerializers:

    @pytest.fixture(scope='class')
    def fpath_retinoblastoma_json(self, fpath_pp: str) -> str:
        """
        Path to a JSON file with retinoblastoma phenopacket.

        Note: the phenopacket is pulled from *Phenopacket tools*.
        """
        return os.path.join(fpath_pp, 'retinoblastoma.json')

    @pytest.fixture
    def serializer(self) -> JsonSerializer:
        return JsonSerializer(indent=2)

    @pytest.fixture
    def deserializer(self) -> JsonDeserializer:
        return JsonDeserializer()

    def test_deserialize(
            self,
            fpath_retinoblastoma_json: str,
            retinoblastoma: Phenopacket,
            deserializer: JsonDeserializer,
    ):
        with open(fpath_retinoblastoma_json) as fh:
            pp = deserializer.deserialize(fh, Phenopacket)

        assert pp == retinoblastoma

    def test_round_trip(
            self,
            retinoblastoma: Phenopacket,
            serializer: JsonSerializer,
            deserializer: JsonDeserializer,
    ):
        # Serialize
        buf = io.StringIO()
        serializer.serialize(retinoblastoma, buf)

        # Deserialize
        buf.seek(0)  # Rewind to allow reading from the buffer.
        out = deserializer.deserialize(buf, Phenopacket)

        # Compare
        assert out == retinoblastoma

    @pytest.mark.skip('Experimental')
    def test_load_many(
            self,
            deserializer: JsonDeserializer,
            serializer: JsonSerializer,
    ):
        fpath_pp = '/home/ielis/ielis/phenopackets/oncoexporter/phenopackets/Colon'
        bla = '/home/ielis/ielis/phenopackets/pyphetools/tmp'
        pps = []
        failed = []
        to_load = os.listdir(fpath_pp)
        print(f'Loading {len(to_load)} phenopackets')
        for fp in to_load:
            full = os.path.join(fpath_pp, fp)
            with open(full) as fh:
                try:
                    pp = deserializer.deserialize(fh, Phenopacket)
                    with open(os.path.join(bla, fp), 'w') as o:
                        serializer.serialize(pp, o)
                    pps.append(pp)
                except ValueError as ve:
                    failed.append((fp, ve.args[0]))

        print(f'Successful: {len(pps)}')
        print(f'Failed: {len(failed)}')
        with open('bla.txt', 'w') as out:
            for f in failed:
                out.write('\t'.join(f))
                out.write('\n')
