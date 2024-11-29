# models/schedule.py

class Schedule:
    def __init__(self, funcion_id, horario, tipo_sala):
        self.funcion_id = funcion_id
        self.horario = horario
        self.tipo_sala = tipo_sala

    @classmethod
    def from_db_row(cls, row):
        return cls(row.FuncionID, row.Horario, row.TipoSala)
