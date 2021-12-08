b=Simulink.Parameter;
b.Value=0.2;
% The storage class decides if and where a parameter is accessible from.
% For 'ExportedGlobal' the parameter will be accesible on the root of the
% model
b.CoderInfo.StorageClass='ExportedGlobal';

k=Simulink.Parameter;
k.Value=1;
% The 'SimulinkGlobal' storage class, will place the parameter in the 
% parameters struct
k.CoderInfo.StorageClass='SimulinkGlobal';


m=Simulink.Parameter;
m.Value=1;
m.CoderInfo.StorageClass='SimulinkGlobal';


Kp=Simulink.Parameter;
Kp.Value=1;
Kp.CoderInfo.StorageClass='SimulinkGlobal';

Ki=Simulink.Parameter;
Ki.Value=1;
Ki.CoderInfo.StorageClass='SimulinkGlobal';

Kd=Simulink.Parameter;
Kd.Value=1;
Kd.CoderInfo.StorageClass='SimulinkGlobal';